/** @odoo-module **/

import { AutoComplete } from "@web/core/autocomplete/autocomplete";
import { patch } from "@web/core/utils/patch";

patch(AutoComplete.prototype, {
    setup() {
        super.setup();
        this.selectedRecords = [];
    },

    selectRecordSelection(ev, indices) {        
        if (ev.target.checked){
            this.selectedRecords.push(indices)
        }
        else {
            this.selectedRecords.pop(indices)
        }
    },

    selectOption(indices, params = {}) {
        if (!this.selectedRecords.length) {
            return super.selectOption(...arguments);
        }
        this.selectedRecords.forEach((indices) => {
            const option = this.sources[indices[0]].options[indices[1]];
            this.inEdition = false;
            if (option.unselectable) {
                this.inputRef.el.value = "";
                this.close();
                return;
            }
            if (this.props.resetOnSelect) {
                this.inputRef.el.value = "";
            }

            this.forceValFromProp = true;
            this.props.onSelect(option, {
                ...params,
                input: this.inputRef.el,
            });
        });
        this.selectedRecords = [];
        this.close();
    }
})