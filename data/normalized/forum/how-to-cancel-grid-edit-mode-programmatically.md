# How to cancel grid edit mode programmatically

## Question

**Rob** asked on 07 Dec 2021

Hi, how can I cancel the edit mode programmatically in Inline edit mode?

## Answer

**Apostolos** answered on 07 Dec 2021

Hi Robert, It is possible to exit edit mode programmatically, without using the default Cancel button. To achieve this, you can use the Grid State. We have a section that shows how to initiate editing. In your case, you will do the opposite - set the following Grid state properties to null: InsertedItem EditItem OriginalEditItem The code snippet bellow uses an OnClick event handler as an example. Note that the edited item will not be saved. <TelerikButton OnClick="@CancelEdit"> Exit Edit Mode </TelerikButton> <TelerikGrid @ref="@GridRef" /> @code {
TelerikGrid <GridModel> GridRef { get; set; }

async Task CancelEdit()
{
var state=GridRef.GetState();
state.EditItem=null;
state.InsertedItem=null;
state.OriginalEditItem=null;
await GridRef.SetState(state);
}
} I hope you find the above information useful. Regards, Apostolos

### Response

**Robert** commented on 07 Dec 2021

Hi Apostolos! Thanks for the answer. A suggestion: why not to provide a simple public method on the Grid?

### Response

**Apostolos** commented on 08 Dec 2021

Hello Robert, Normally, the Grid Cancel command allows users to cancel changes in inline edit mode. It appears that it is not suitable for your case. I would like to get more details about your scenario and what brings the need to exit edit mode programmatically. This will allow us to understand your needs better. Thank you in advance! Regards, Apostolos

### Response

**Leland** commented on 13 Sep 2024

I can confirm that using the Grid State in this way still works. However, I want to point out that `OriginalEditItem`, `EditItem`, and `InsertedItem` are non-nullable types, so you get a warning that you cannot convert null literal to non-nullable reference type. Making them nullable would remove the warning and better communicate the intent that setting a null value can cancel the edit.

### Response

**Dimo** commented on 16 Sep 2024

@Leland - I agree with you and I stumble on this issue myself. We have an internal task about nullable-related refactoring in our source code. The bad thing is that this task requires development effort, which does not match the resulting small business value. As a result, the priority is low. Please consider the null forgiving operator, if you haven't already.
