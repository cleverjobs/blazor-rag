# Telerik Button Focus

## Question

**Vis** asked on 24 Aug 2021

Hi Is Focus is available for Telerik Button? Could you please suggest on this? Thanks, Vishnu Vardhanan H

## Answer

**Hristian Stefanov** answered on 27 Aug 2021

Hi Vishnu, You can programmatically focus any specific button using the FocusAsync() method the TelerikButton provides. I have prepared for you an example showing a possible implementation of the functionality: <TelerikButton OnClick="@FocusMyButton">Focus the second button!</TelerikButton>
<br />
<br />
<br />
@result
<br />
<TelerikButton @ref="@button" OnClick="@OnClickHandler">Second button!</TelerikButton>

@code { string result; string moreInfo; TelerikButton button; async Task FocusMyButton ( ) { await button.FocusAsync();
} async Task OnClickHandler ( MouseEventArgs args ) {
result="Second Button was clicked at: " + DateTime.Now.ToString();
}
} You can find more details and examples regarding the FocusAsync() method in the following knowledge base article: Focus TextBox Programmatically. I hope this helps. Please let me know if you need any further information. Regards, Hristian Stefanov Progress Telerik
