from gluon.contrib.appconfig import AppConfig

myconf = AppConfig(reload=True)


if not request.env.web2py_runtime_gae:
    
    db = DAL(myconf.take('db.uri'), pool_size=myconf.take('db.pool_size', cast=int), check_reserved=['all'])
else:
    
    db = DAL('google:datastore+ndb')
    session.connect(request, response, db=db)

response.generic_patterns = ['*'] if request.is_local else []
## choose a style for forms
response.formstyle = myconf.take('forms.formstyle')  # or 'bootstrap3_stacked' or 'bootstrap2' or other
response.form_label_separator = myconf.take('forms.separator')

from gluon.tools import Auth, Service, PluginManager

auth = Auth(db)
service = Service()
plugins = PluginManager()

## create all tables needed by auth if not custom tables
auth.define_tables(username=False, signature=False)

## configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else myconf.take('smtp.sender')
mail.settings.sender = myconf.take('smtp.sender')
mail.settings.login = myconf.take('smtp.login')

auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

db.define_table('product',
    Field('name','string',requires=IS_NOT_EMPTY()),
    Field('price','integer',requires=IS_NOT_EMPTY()),
    Field('description','text'),
    Field('image','upload'),
    Field('category','string'),
    Field('sub','string'),
    Field('mini','string'),
    )

db.define_table('bill',
    Field('creditcard','string',requires=IS_NOT_EMPTY()),
    Field('expirydate','string',default='12/2012'),
    Field('CVV','integer',requires=IS_NOT_EMPTY())
    )
db.define_table('address',
    Field('Phone Number','integer',requires=IS_NOT_EMPTY()),
    Field('Adress','string',default='12/2012'),
    Field('City','string',requires=IS_NOT_EMPTY())
    )

                
session.cart = session.cart or {}
auth.enable_record_versioning(db)
