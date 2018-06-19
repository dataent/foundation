<!-- add-breadcrumbs -->
# Anliegen der Lagerbuchung einschränken
<span class="text-muted contributed-by">Beigetragen von CWT Connector & Wire Technology GmbH</span>

    dataent.ui.form.on("Material Request", "validate", function(frm) {
        if(user=="user1@example.com" && frm.doc.purpose!="Material Receipt") {
            dataent.msgprint("You are only allowed Material Receipt");
            dataent.throw(__("Not allowed"));
        }
    }

{next}
