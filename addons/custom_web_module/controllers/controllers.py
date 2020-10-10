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
        return request.render('website.homepage')


class CheckoutForm(http.Controller):
    @http.route(['/checkout/form/submit'], type='http', auth="public", website=True, csrf=False)
    def new_checkout(self, **post):
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
        }

        product = request.env['product.template'].search([('ilike','=','value')])

        print (posted_dict)
#     @http.route('/custom_web_homepage/custom_web_homepage/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_web_homepage.listing', {
#             'root': '/custom_web_homepage/custom_web_homepage',
#             'objects': http.request.env['custom_web_homepage.custom_web_homepage'].search([]),
#         })

#     @http.route('/custom_web_homepage/custom_web_homepage/objects/<model("custom_web_homepage.custom_web_homepage"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_web_homepage.object', {
#             'object': obj
#         })