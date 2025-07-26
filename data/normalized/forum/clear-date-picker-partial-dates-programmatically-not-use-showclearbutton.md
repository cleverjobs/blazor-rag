# Clear Date Picker Partial Dates Programmatically (Not Use ShowClearButton)

## Question

**JoeJoe** asked on 01 Apr 2025

Hello, I have a 2 date pickers. I have a button that clears all fields in my form which works when the dates are fully filled, but not if they are partially filled. I want to clear them with my button and not have to use the ShowClearButton (x button) that is built into the date picker. Not sure if there is already a solution for this, but I could not find one.

### Response

**Anislav** commented on 01 Apr 2025

I'm not sure what you mean by the dates being "partially filled." Are you referring to a scenario where one of the date pickers is filled while the other is not? Could you share the code you’re using to clear the fields? In general it would be helpful if you could provide a sample demonstrating the issue using this site: Blazor REPL.

### Response

**Joe** commented on 01 Apr 2025

Below is a screenshot of the partially filled. I believe when it's partially filled, it is considered "null" still because the value isn't actually saved. The date picker values are tied to an object "email pay". I'm trying to use ClearObject.ResetProperties(emailPay); to clear the fields. It will work if the date is completely filled (i.e. 12/12/25). Currently the way I've had to solve this is by manually setting the values to a full date and then setting them back to null. emailPay.InvoiceDate=DateTime.Now; emailPay.InvoiceDueDate=DateTime.Now; await Task.Delay(1); emailPay.InvoiceDate=null; emailPay.InvoiceDueDate=null; I was just curious if there was a more elegant solution than just manually resetting it.

### Response

**Joe** commented on 02 Apr 2025

<TelerikDatePicker @bind-Value="@DateToClear" ShowWeekNumbers="true" Format="MM/dd/yy"> </TelerikDatePicker> <button @onclick="ClearField"> Clear Field </button> <button @onclick="MyCurrentFix"> Clear Field Hacky Way </button> @code {
DateTime? DateToClear {get; set;}=null;

//This only works if the date is partially filled (fill only part of date picker so it gives error)
private void ClearField()
{
DateToClear=null;
StateHasChanged();
}

// currently the fix that I have below, but it's really hacky (this can clear partially filled dates)

private async Task ResetDate()
{
DateToClear=DateTime.Now;
await Task.Delay(1);
DateToClear=null;
}

private async Task MyCurrentFix()
{
await ResetDate();
StateHasChanged();
}
}

### Response

**Joe** commented on 02 Apr 2025

I couldn't figure out how to save the code in the REPL link, but this is what I was putting in there and it works in terms of demonstrating the issue

### Response

**Anislav** commented on 02 Apr 2025

You need to click the "Share Snippet" button at the top right. This will save your code and generate a shareable link.

## Answer

**Anislav** answered on 02 Apr 2025

I got what you are trying to achieve. The issue arises because partially entered data is not assigned to the value of the date picker, which remains null. So, when you attempt to clear it by setting it to null again, Blazor doesn't recognize a state change, even if you explicitly call StateHasChanged(). A potential workaround is to add a JavaScript function that takes the ID of the picker component. When called, it locates the corresponding HTML element using the data-id attribute and clears its value. Regards, Anislav Atanasov

### Response

**Joe** commented on 02 Apr 2025

I might be a little confused on what to do. I grabbed the element by its id. Then i tried to grab the element by the data-id and then update the elements value. The result is it clears the field but now there are no placeholders and the errors are still there. But when I click on the date picker anywhere, it comes back to what it was before. function clearDatePickers() {
console.log("clearDatePickers function called");

let invoiceDatePicker=document.getElementById("txtInvoiceDate_EP");
let invoiceDueDatePicker=document.getElementById("txtInvoiceDueDate_EP");

if (invoiceDatePicker) {
let invoiceDatePickerDataID=invoiceDatePicker.getAttribute("data-id");
if (invoiceDatePickerDataID) {
let datePickerElement=document.querySelector(`[data-id='${invoiceDatePickerDataID}']`);
if (datePickerElement) {
datePickerElement.value=null;
console.log(`Cleared value of date picker with data-id: ${invoiceDatePickerDataID}`);
}
else {
console.warn(`No date picker found with data-id: ${invoiceDatePickerDataID}`);
}
}
else {
console.warn("No data-id attribute found on invoiceDatePicker");
}
}
else {
console.warn("No data-id attribute found on invoiceDatePicker");
}

if (invoiceDueDatePicker) {
let invoiceDueDatePickerDataID=invoiceDueDatePicker.getAttribute("data-id");
if (invoiceDueDatePickerDataID) {
let datePickerElement=document.querySelector(`[data-id='${invoiceDueDatePickerDataID}']`);
if (datePickerElement) {
datePickerElement.value=null;
console.log(`Cleared value of date picker with data-id: ${invoiceDueDatePickerDataID}`);
}
else {
console.warn(`No date picker found with data-id: ${invoiceDueDatePickerDataID}`);
}
}
else {
console.warn("No data-id attribute found on invoiceDueDatePicker");
}
}
else {
console.warn("No element found with ID: txtInvoiceDueDate_EP");
}
}

### Response

**Anislav** commented on 02 Apr 2025

My mistake, I didn't consider the validation. I'll explore another workaround. Would it be acceptable to have default values for the date pickers, such as 'today' and 'yesterday,' instead of null?

### Response

**Joe** commented on 02 Apr 2025

As far as I Know, the preferred approach would be to have the value at null to keep the placeholder of MM/DD/YYYY showing.
