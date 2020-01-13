{
    'name': "Education Payment System",
    'version': '1.0',
    'depends': ["web", "base", "website"],
    'data': [
        'security/ir.model.access.csv',
        'views/eps_university.xml',
        'views/institute.xml',
        'views/cource.xml',
        'views/template.xml',
        'views/student.xml',
        'wizard/wizard_view.xml',
        'reports/report_invoice_with_payments.xml',
        'reports/reports_institute.xml',
    ],
}
