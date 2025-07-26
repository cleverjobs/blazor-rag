# k-invalid Styling is Removed for Custom ValidationAttribute

## Question

**Lel** asked on 19 Aug 2024

Please see the following minimal reproducible example: [https://blazorrepl.telerik.com/GeYMbZQk22cmnlsN33](https://blazorrepl.telerik.com/GeYMbZQk22cmnlsN33) When adding a new record and editing `Field1`, the validation tooltip and k-invalid styling appear if the user is entering any value that triggers the custom ValidationAttribute. If the user presses enter, the validation correctly prevents a new record from being created. However, k-invalid styling is replaced with k-valid styling, and the validation tooltip disappears. How can the k-invalid styling and validation tooltip persist when the user presses enter with an invalid input?

## Answer

**Hristian Stefanov** answered on 21 Aug 2024

Hi Leland, I confirm that your observations on the current behavior are correct. To address this scenario, a public item for an enhancement in the Incell and Inline editing has already been submitted on our public

### Response

**Leland** commented on 21 Aug 2024

The linked feature request doesn't address the issue of k-invalid styling disappearing when the user attempts to create or update an invalid row. In fact, it seems to be requesting a change that would only aggravate my issue. It states "When I override the IsValid method to return a ValidationResult the Incell & Inline edit modes allow the editing to be continued even if an invalid value is present." This describes the current behavior, and is actually desired. The editing needs to continue so that the user has the opportunity to correct whatever is causing the validation issue, but there needs to be styling to indicate which rows have the issues, along with tooltips to provide details in complex scenarios. If they wish to abandon the edit, they can still press a cancel command button, if present (I excluded one from my example, for simplicity). I also note that there is no workaround to use until this is implemented, as is common in other bug reports or feature requests I have seen. Can anything be done now to get the k-invalid styling to persist in this situation?

### Response

**Hristian Stefanov** commented on 23 Aug 2024

Hi Leland, Thank you for getting back to me. Your feedback on the linked feature request suggests that the description might not be clear enough. When it says, "the Incell & Inline edit modes allow editing to continue even if an invalid value is present," it means users can move to the next cell without correcting the invalid input, which is not the intended behavior. The correct approach should prevent moving forward until a valid value is entered, with the red border persisting until then. You are right that there isn’t a workaround at the moment. If any workaround becomes available, I’ll share it in the comments of the public item. Let me know if I'm still missing something from the scenario. Kind Regards, Hristian

### Response

**Leland** commented on 23 Aug 2024

Keeping the user in a cell with invalid input can be helpful, but doesn't solve all scenarios with this issue. For instance, in a grid with many columns, some optional and some not, the user may not have yet visited a required column and press enter. The validation prevents the row from being created/updated, but the issue means k-valid styling is displayed, so they have no idea which column is preventing the action. k-valid styling being applied when validation is preventing row creation / updating seems like a bug.

### Response

**Hristian Stefanov** commented on 28 Aug 2024

Hi Leland, I confirm that the k-valid styling isn't being applied correctly because Grid Incell & Inline Editing currently doesn't work with ValidationResult for custom validation attributes. Rest assured, the item I linked will fully cover your scenario and display the validation CSS class correctly. Keep an eye on it for further updates. Kind Regards, Hristian
