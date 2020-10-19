# -*- coding: utf-8 -*-
from odoo import http
from odoo.addons.portal.controllers.web import Home
from odoo.http import request


class CustomWebHomepage(Home):
    @http.route(auth="public")
    def index(self, **kw):
        #invoices = request.env['account.invoice'].sudo().search([])
        #import pdb;pdb.set_trace()
        super(CustomWebHomepage, self).index()
        categories = request.env['hotel.room.type'].sudo().search([])
        amenities = request.env['hotel.room.amenities'].sudo().search([])
        services = request.env['hotel.services'].sudo().search([])
        context = {
            "categories": categories,
            "amenities": amenities,
            "services": services
        }
        return request.render('custom_web_module.homepage', context)

    @http.route(['/aboutus'], type='http', auth="public", website=True)
    def about(self, **post):
        context = {}
        return request.render('custom_web_module.custom_about', context)

    @http.route(['/contactus'], type='http', auth="public", website=True)
    def contact(self, **post):
        context = {}
        return request.render('custom_web_module.custom_contact_us', context)


class CheckoutForm(http.Controller):
    @http.route(['/checkout/form/submit'], type='http', auth="public", website=True, csrf=False)
    def new_checkout(self, **post):
        customer_obj = request.env['res.partner']
        reservation_obj = request.env['hotel.reservation']
        reservation_line_obj = request.env["hotel_reservation.line"]

        print("POSTED DATA", post)
        posted_dict = {
            "appart_type": post.get("appart_type"),
            "address": post.get("whole_address"),
            "3rooms": post.get("category_3rooms"),
            "2rooms": post.get("category_2rooms"),
            "3rooms_qty": post.get("category_3rooms_qty"),
            "2rooms_qty": post.get("category_2rooms_qty"),
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
            "services_ids": request.httprequest.form.getlist('services_ids'),
            "amenities_ids": request.httprequest.form.getlist('amenities_ids'),
        }

        print("DICT CLEANNED DATA", post)

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

        if "3rooms" == posted_dict["3rooms"]:
            category = request.env['hotel.room.type'].search([('slug', '=', posted_dict["3rooms"])])
            rooms = request.env['hotel.room'].search([('categ_id', '=', category.id), ('status', '=', 'available')])

            if rooms:
                tab = []
                for room in rooms:
                    tab.append(room.id)

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

        elif "2rooms" == posted_dict["2rooms"]:
            category = request.env['hotel.room.type'].search([('slug', '=', posted_dict["2rooms"])])
            rooms = request.env['hotel.room'].search([('categ_id', '=', category.id)])

            if rooms:
                tab = []
                for room in rooms:
                    tab.append(room.id)

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
        else:
            context_value = "Aucune catégorie de ce type sélectionnée"
            print("Error on reservation, due to rooms type", context_value)
            pass

        # context = {
        #    #"value": context_value
        #    "value": "context_value"
        # }
        # return request.render('custom_web_module.custom_homepage_view', context)

    @http.route(['/contact/form/submit'], type='http', auth="public", website=True, csrf=False)
    def contact_form(self, **post):
        print("Posted!!!!!!!!", post)