/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { BarcodeParser } from "@barcodes/js/barcode_parser";

console.log('Loaded!');
console.log(BarcodeParser)

patch(BarcodeParser.prototype, {
    match_pattern(barcode, pattern, encoding){
        console.log("Override Match_Pattern function");
        console.log(barcode);
        console.log(pattern);
        console.log(encoding);
        if (pattern === "2.....{NNDDDD}" || pattern === "21....{NNDDDD}") {
            console.log(barcode.slice(0, 10));
            barcode = barcode.slice(0, 11);
            console.log(barcode);
        }
        return super.match_pattern(barcode, pattern, encoding);
    },
});