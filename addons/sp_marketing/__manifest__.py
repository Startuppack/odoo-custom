{
    # Email marketing for every Startup Pack tenant: campaigns to CRM leads
    # (open/click/reply stats, mailing lists, unsubscribe + blacklist), with
    # replies linked back to the leads. No code of its own: it only pulls the
    # core modules in, so the chart can install one module on every tenant.
    "name": "Startup Pack: email marketing",
    "version": "18.0.1.0.0",
    "summary": "Install Odoo Email Marketing with its CRM integration.",
    "author": "Startup Pack",
    "license": "LGPL-3",
    "category": "Marketing/Email Marketing",
    "depends": ["mass_mailing", "mass_mailing_crm"],
    "data": [],
    "installable": True,
    "auto_install": False,
}
