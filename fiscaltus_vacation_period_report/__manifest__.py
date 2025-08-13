{
    "name": "Vacaciones por Período (Aniversario) - FISCALTUS",
    "version": "18.0.1.0",
    "category": "Human Resources",
    "summary": "Reporte de vacaciones pendientes por período aniversario (FIFO).",
    "depends": ["hr_holidays", "hr", "hr_contract"],
    "data": [
        "security/ir.model.access.csv",
        "views/vacation_report_views.xml",
        "data/cron.xml",
    ],
    "license": "OPL-1",
    "application": False,
    "installable": True,
}
