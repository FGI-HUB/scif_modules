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
        return request.render('scif_web_template.homepage', context)


class ScifWebController(http.Controller):
    @http.route('/gallery', type='http', auth='public', website=True)
    def gallery_view(self, **kwagrs):
        context = {}
        return request.render('scif_web_template.gallery', context)

    @http.route('/booking', type='http', auth='public', website=True)
    def booking_view(self, **kwagrs):
        categories = request.env['hotel.room.type'].sudo().search([])
        amenities = request.env['hotel.room.amenities'].sudo().search([])
        services = request.env['hotel.services'].sudo().search([])
        context = {
            "categories": categories,
            "amenities": amenities,
            "services": services
        }
        return request.render('scif_web_template.booking', context)

    @http.route('/about', type='http', auth='public', website=True)
    def about_view(self, **kwagrs):
        context = {}
        return request.render('scif_web_template.about', context)

    @http.route('/contact', type='http', auth='public', website=True)
    def contact_view(self, **kwagrs):
        context = {}
        return request.render('scif_web_template.contact', context)