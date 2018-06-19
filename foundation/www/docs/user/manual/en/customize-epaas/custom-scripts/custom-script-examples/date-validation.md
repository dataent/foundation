<!-- add-breadcrumbs -->
# Date Validation


	dataent.ui.form.on("Task", "validate", function(frm) {
        if (frm.doc.from_date < get_today()) {
            dataent.msgprint(__("You can not select past date in From Date"));
            dataent.validated = false;
        }
	});

{next}
