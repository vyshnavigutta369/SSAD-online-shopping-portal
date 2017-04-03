def index():
    product = db(db.product).select(orderby=db.product.name)
    return locals()

def form():
    return dict

def search():
    return dict(form=FORM(INPUT(_id='keyword',_name='keyword',_onkeyup="ajax('callback',['keyword'],'target');")),target_div=DIV(_id='target'))

def contact():
    query=db(db.address.id==auth.user.id)
    return dict(message=T("Your order will be placed in 4 days"))

def callback():
    query = (db.product.name.contains(request.vars.keyword)) | (db.product.category.contains(request.vars.keyword)) | (db.product.mini.contains(request.vars.keyword)) | (db.product.sub.contains(request.vars.keyword))
    pages = db(query).select(orderby=db.product.name)
    links = [A(p.name,_href=URL('default','display',args=p.id)) for p in pages ]
    return UL(*links)

def display():
    kick=db.product(request.args(0,cast=int))
    return dict(kick=kick)

def call():
    session.forget()
    return service()
# an action to see and process a shopping cart
@auth.requires_login()
def cart():
    if not session.cart:
        session.flash = 'Add something to shopping cart'
        redirect(URL('index'))
    return dict(cart=session.cart)
@auth.requires_login()
def cart_callback():
    id = int(request.vars.id)
    if request.vars.action == 'add':
        session.cart[id]=session.cart.get(id,0)+1
    if request.vars.action == 'sub':
        session.cart[id]=max(0,session.cart.get(id,0)-1)
    return str(session.cart[id])

@auth.requires_login()
def buy2():
    if not session.cart:
        session.flash = 'Add something to shopping cart'
        redirect(URL('index'))
    import uuid
    from gluon.contrib.AuthorizeNet import process
    total = sum(db.product(id).price*qty for id,qty in session.cart.items())
    form = SQLFORM.factory(
                Field('creditcard',requires=IS_NOT_EMPTY()),
                Field('expiration',default='12/2012',requires=IS_MATCH('\d{2}/\d{4}')),
                Field('cvv',requires=IS_MATCH('\d{3}')))
    if form.accepts(request,session):
        if process(form.vars.creditcard,form.vars.expiration,
                    total,form.vars.cvv,0.0,invoice,testmode=True):
            for key, value in session.cart.items():
                db.sale.insert( buyer=auth.user.id,
                                product = key,
                                quantity = value,
                                price = db.product(key).price,
                                creditcard = form.vars.creditcard)
            session.cart.clear()
            session.flash = 'Thank you for your order'
        else:
            response.flash = "payment rejected (please call XXX)"
    return dict(cart=session.cart,form=form,total=total)

def addres():
    db.address.insert(id=auth.user.id,
                      )
    form=SQLFORM(db.address).process()
    if form.accepted:
        redirect(URL('contact'))
    return dict(form=form)



@auth.requires_login()
def buy():
    if not session.cart:
        session.flash = 'Add something to shopping cart'
        redirect(URL('index'))
    form=SQLFORM(db.bill).process()
    if form.accepted:
        redirect(URL('default','addres'))
    return dict(form=form)

@auth.requires_membership('admin')
def sale():
    form=SQLFORM(db.product).process()
    if form.accepted:
        redirect(URL('default','contact us'))
    return dict(form=form)
    
def biography():
    biography = db((db.product.category=='books') & (db.product.sub=='biography')).select(orderby=db.product.name)
    return locals()    
def ac():
    ac = db((db.product.category=='homeneeds') & (db.product.sub=='ac')).select(orderby=db.product.name)
    return locals()
def fiction():
    fiction = db((db.product.category=='books') & (db.product.sub=='fiction')).select(orderby=db.product.name)
    return locals()
def history():
    phones = db((db.product.category=='books') & (db.product.sub=='history')).select(orderby=db.product.name)
    return locals()
def ipads():
    ipads = db((db.product.category=='electrical appliances') & (db.product.sub=='ipads')).select(orderby=db.product.name)
    return locals()
def kidaccess():
    kidaccess = db((db.product.category=='kids') & (db.product.sub=='kidaccess')).select(orderby=db.product.name)
    return locals()
def kidcloth():
    kidcloth = db((db.product.category=='kids') & (db.product.sub=='kidcloth')).select(orderby=db.product.name)
    return locals()
def philosophy():
    philosophy = db((db.product.category=='books') & (db.product.sub=='philosophy')).select(orderby=db.product.name)
    return locals()
def kidfoot():
    kidfoot = db((db.product.category=='kids') & (db.product.sub=='kidfoot')).select(orderby=db.product.name)
    return locals()
def laptops():
    laptops = db((db.product.category=='electrical appliances') & (db.product.sub=='laptops')).select(orderby=db.product.name)
    return locals()
def maccessories():
    maccessories = db((db.product.category=='men') & (db.product.sub=='maccessories')).select(orderby=db.product.name)
    return locals()
def mclothing():
    mclothing = db((db.product.category=='men') & (db.product.sub=='mclothing')).select(orderby=db.product.name)
    return locals()
def mfootwear():
    mfootwear = db((db.product.category=='men') & (db.product.sub=='mfootwear')).select(orderby=db.product.name)
    return locals()

def phones():
    phones = db((db.product.category=='electrical appliances') & (db.product.sub=='phones')).select(orderby=db.product.name)
    return locals()
def sciefi():
    sciefi = db((db.product.category=='books') & (db.product.sub=='sciefi')).select(orderby=db.product.name)
    return locals()
def tablets():
    tablets = db((db.product.category=='electrical appliances') & (db.product.sub=='tablets')).select(orderby=db.product.name)
    return locals()
def waccess():
    waccess = db((db.product.category=='women') & (db.product.sub=='waccess')).select(orderby=db.product.name)
    return locals()
def wcloth():
    wcloth = db((db.product.category=='women') & (db.product.sub=='wcloth')).select(orderby=db.product.name)
    return locals()
def wfoot():
    wfoot = db((db.product.category=='women') & (db.product.sub=='wfoot')).select(orderby=db.product.name)
    return locals()
def furniture():
    furniture = db((db.product.category=='homeneeds') & (db.product.sub=='furniture')).select(orderby=db.product.name)
    return locals()
def tv():
    tv = db((db.product.category=='homeneeds') & (db.product.sub=='tv')).select(orderby=db.product.name)
    return locals()
def refrigerators():
    refrigerators = db((db.product.category=='homeneeds') & (db.product.sub=='refrigerators')).select(orderby=db.product.name)
    return locals()

             
def user():
    if auth.is_logged_in() and request.url.split('/')[-1]=='login':
        redirect(URL('default','index'))
    return dict(form=auth())
@cache.action()
def download():
    return response.download(request, db)
