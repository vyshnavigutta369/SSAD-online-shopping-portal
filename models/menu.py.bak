#response.logo = A(B('YOROCK')),
response.menu = [
    (T('HOME'), False, URL('default', 'index'), [])
]
DEVELOPMENT_MENU = True
def _():
    app = request.application
    ctr = request.controller
    response.menu += [
         (T('SEARCH'),False,URL('default','search')),
         (T('ELECTRICAL APPLIANCES'), False, '#', [
              (T('Phones'), False, URL('default','phones')),
              (T('Ipads'), False, URL('default','ipads')),
              (T('Laptops'), False, URL('default','laptops')),
              (T('Tablets'), False, URL('default','tablets')),
              ]),
            (T('BOOKS'), False, '#', [
              (T('Fiction'), False, URL('default','fiction')),
              (T('Philosophy'), False, URL('default','philosophy')),
              (T('Sci-fi'), False, URL('default','sciefi')),
              (T('Biographies'), False, URL('default','biography')),
              (T('History'), False, URL('default','history')),
              ]),
            (T('MEN'), False, '#', [
              (T('Clothing'), False, URL('default','mclothing')),
              (T('Footwear'), False, URL('default','mfootwear')),
              (T('Accessories'), False, URL('default','maccessories')),
              ]),
            (T('WOMEN'), False, '#', [
              (T('Clothing'), False, URL('default','wcloth')),
              (T('Footwear'), False, URL('default','wfoot')),
              (T('Accessories'), False, URL('default','waccess')),
              ]),
            (T('KIDS'), False, '#', [
              (T('Clothing'), False, URL('default','kidcloth')),
              (T('Footwear'), False, URL('default','kidfoot')),
              (T('Accessories'), False, URL('default','kidaccess')),
              ]),
            (T('HOMENEEDS'), False, '#', [
              (T('Furniture'), False, URL('default','furniture')),
              (T('TV'), False, URL('default','tv')),
              (T('Refrigerators'), False, URL('default','refrigerators')),
              (T('Air Conditioners'), False, URL('default', 'ac')),
              ]),
            (T('MY CART'), False, URL('default','cart')),
            (T('BUY'),False,URL('default','buy')),
            (T('RETAILER'),False,URL('default','sale')),
            (T('CONTACT US'),False,URL('default','contact')),
            (T('MANAGE'),False,URL('appadmin','index')),
            
         ]
if DEVELOPMENT_MENU: _()

if "auth" in locals(): auth.wikimenu()
