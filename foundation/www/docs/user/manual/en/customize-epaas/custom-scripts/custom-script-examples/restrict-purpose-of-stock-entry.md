<!-- add-breadcrumbs -->
# Restrict Purpose Of Stock Entry


    dataent.ui.form.on("Material Request", "validate", function(frm) {
        if(dataent.user=="user1@example.com" && frm.doc.purpose!="Material Receipt") {
            dataent.msgprint("You are only allowed Material Receipt");
            dataent.throw(__("Not allowed"));
        }
    }


{next}
