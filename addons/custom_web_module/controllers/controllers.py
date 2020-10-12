# -*- coding: utf-8 -*-
from odoo import http
from odoo.addons.portal.controllers.web import Home
from odoo.http import request


class CustomWebHomepage(Home):
    @http.route()
    def index(self, **kw):
        #invoices = request.env['account.invoice'].sudo().search([])
        #import pdb;pdb.set_trace()
        super(CustomWebHomepage, self).index()
        categories = request.env['hotel.room.type'].search([])
        context = {
            "categories": categories
        }
        return request.render('website.homepage', context)


class CheckoutForm(http.Controller):
    @http.route(['/checkout/form/submit'], type='http', auth="public", website=True, csrf=False)
    def new_checkout(self, **post):
        customer_obj = request.env['res.partner']
        reservation_obj = request.env['hotel.reservation']
        reservation_line_obj = request.env["hotel_reservation.line"]

        posted_dict = {
            "appart_type": post.get("appart_type"),
            "app_nber": post.get("app_nber"),
            "start_date": post.get("start_date"),
            "end_date": post.get("end_date"),
            "old": post.get("old"),
            "invalid": post.get("invalid"),
            "allergic": post.get("allergic"),
            "child": post.get("child"),
            "name": post.get("name"),
            "surname": post.get("surname"),
            "email": post.get("email"),
            "phone": post.get("phone"),
            "child_number": post.get("child_number"),
            "adult_number": post.get("adult_number"),
            "floor": post.get("floor"),
        }

        import pdb; pdb.set_trace()
        print(posted_dict)

        # Check if a client with this email is available on the system
        user = request.env['res.partner'].search([('email', '=', posted_dict["email"])])
        if user.id:
            # If user exist, make reservation with the user account
            customer = user
        else:
            # Create a new client
            name = "%s %s" % (posted_dict["name"], posted_dict["surname"])
            email = posted_dict["email"]
            phone = posted_dict["phone"]
            company_type = "person"
            user_val = {
                "name": name,
                "email": email,
                "phone": phone,
                "company_type": company_type,
            }
            customer = customer_obj.sudo().create(user_val)

        if(posted_dict["appart_type"]):
            if ("3rooms" == posted_dict["appart_type"]):
                # TODO Check if category and if room... Else return a same page with context value to display, like
                #  flash message
                category = request.env['hotel.room.type'].search([('name', '=', 'Appartement de trois chambres')])
                # TODO Write a domain to find only one user with categ_id egal to selected categ and with status
                rooms = request.env['hotel.room'].search([('categ_id', '=', category.id), ('status', '=', 'available')])

                if rooms:
                    tab = []
                    for room in rooms:
                        tab.append(room.id)
                    # If rooms is not empty, process operation
                    print("EXcept code room tab", tab)

                    # Now we are creating a reservation object
                    reservation = reservation_obj.sudo().create(
                        {
                            "partner_id": customer.id,
                            "warehouse_id": 1,
                            "pricelist_id": 1,
                            "checkin": posted_dict["start_date"],
                            "adults": posted_dict["adult_number"],
                            "children": posted_dict["child_number"],
                            "checkout": posted_dict["end_date"],
                        }
                    )

                    reservation_line = reservation_line_obj.sudo().create(
                        {
                            "name": "Line-%s" %(customer.name),
                            "line_id": reservation.id,
                            "categ_id": category.id,
                            "reserve": [(6, 0, tab)]
                        }
                    )

            elif ("2rooms" == posted_dict["appart_type"]):
                # TODO Check if category and if room... Else return a same page with context value to display, like
                #  flash message
                category = request.env['hotel.room.type'].search([('name', '=', 'Appartement de deux chambres')])
                # TODO Write a domain to find only one user with categ_id egal to selected categ and with status
                rooms = request.env['hotel.room'].search([('categ_id', '=', category.id)])
            else:
                context_value = "Aucune catégorie de ce type sélectionnée"

        # TODO check if room is list or a single value. Anyway, reate for statement and adding reservation line,



        print ("Notre reservation",reservation)
        context = {
            #"value": context_value
            "value": "context_value"
        }

        #return request.render('custom_web_module.custom_homepage_view', context)


class CheckoutForm(http.Controller):
    @http.route(['/aboutus'], type='http', auth="public", website=True)
    def new_checkout(self, **post):
        context = {}
        return request.render('custom_web_module.custom_homepage_view', context)