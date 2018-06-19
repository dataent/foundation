<!-- add-breadcrumbs -->
# Datenvalidierung
<span class="text-muted contributed-by">Beigetragen von CWT Connector & Wire Technology GmbH</span>

	dataent.ui.form.on("Event", "validate", function(frm) {
        if (frm.doc.from_date < get_today()) {
            dataent.msgprint(__("You can not select past date in From Date"));
            dataent.throw(__("past date selected"))
        }
	});

{next}
