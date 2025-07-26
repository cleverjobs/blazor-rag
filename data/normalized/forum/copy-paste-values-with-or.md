# Copy/Paste Values with ',' or '.'

## Question

**Mar** asked on 02 Apr 2024

We use a NumericTextbox for amounts. The "Format" parameter is set to "###,###,###,###,##0.00". It should now be possible to copy already formatted numeric values (with thousands separator) into the textbox. However, this only accepts unformatted numerical values: 100000 <-- works 100000,23 <-- works 100,000.23 <-- does not work Depending on the language/culture, the thousands separator changes (either '.' or ','). As soon as the number contains a thousands separator, the textbox no longer recognises the value as a number and does not accept the value. Is there a way to achieve this?

## Answer

**Hristian Stefanov** answered on 02 Apr 2024

Hi Martin, A feature request for the desired functionality in our TelerikNumericTextbox has already been submitted on our public feedback portal: Allow formatted numbers (e.g. 1,234,567.89) to be pasted into a NumericTextBox. I voted for it on your behalf and raised its priority. You can check out the public item and also subscribe to receive email notifications for status updates. Regards, Hristian Stefanov Progress Telerik
