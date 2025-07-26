# Inline Edit Specify Initial Column Focus

## Question

**Lel** asked on 02 Jul 2024

When using a grid in `GridEditMode.Inline`, the first column is always focused for editing. I need the second column to always be when beginning to insert or edit a row. How can this be achieved?

## Answer

**Tsvetomir** answered on 05 Jul 2024

Hello Leland, We have an open feature request in our feedback portal for the desired functionality: Specifying which field should have focus in Grid editor. I voted for it on your behalf and raised its priority. In the meantime, you can refer to the workaround in the linked item. In your case, you need only one EditorTemplate for the column that will receive focus. The OnRowClick event is not necessary either. You can also subscribe to the item to get notified of any status updates via email. Regards, Tsvetomir Progress Telerik
