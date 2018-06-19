<!-- add-breadcrumbs -->
# Abbruchrechte einschränken
<span class="text-muted contributed-by">Beigetragen von CWT Connector & Wire Technology GmbH</span>

Fügen Sie dem Ereignis custom_before_cancel eine Steuerungsfunktion hinzu:

    cur_frm.cscript.custom_before_cancel = function(doc) {
        if (dataent.user_roles.indexOf("Accounts User")!=-1 && dataent.user_roles.indexOf("Accounts Manager")==-1
                && user_roles.indexOf("System Manager")==-1) {
            if (flt(doc.grand_total) > 10000) {
                dataent.msgprint("You can not cancel this transaction, because grand total \
                    is greater than 10000");
                dataent.validated = false;
            }
        }
    }


{next}
