from odoo import http
from odoo.http import request


class StudentDetails(http.Controller):

    @http.route('/sestion/', auth='public', website=True)
    def index(self, **kw):
        record = request.env['courece.cource'].search([])
        return request.render('vishal-trainee-eps.index', {
            "record": record,
        })

    @http.route(["/sestion/create"], auth="public", website=True, csrf=False)
    def insert(self, **kw):
        if request.httprequest.method == "POST":
            request.env["courece.cource"].create({
                'courece_name': request.params.get("txt_cname"),
                'courece_fees': request.params.get("txt_fees"),
            })
            return request.redirect("/sestion/")
        return request.render('vishal-trainee-eps.insert', {"record": False})

    @http.route('/sestion/delete/<model("courece.cource"):cource>', type="http", auth="public", website=True, csrf=False)
    def delete(self, cource=None):
        if cource:
            print("cource")
            cource.unlink()
        return http.request.redirect("/sestion/")

    @http.route('/sestion/edit/<model("courece.cource"):cource>', type="http", auth="public", website=True, csrf=False)
    def edit(self, cource=None):
        if request.httprequest.method == "POST":
            cource.write({
                'courece_name': request.params.get("txt_cname"),
                'courece_fees': request.params.get("txt_fees"),
            })
        return request.render('vishal-trainee-eps.insert', {
            "record": cource,
        })