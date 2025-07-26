# Execute Method only on Enter for Text Box.

## Question

**Luk** asked on 22 May 2020

I want to be able to use either the enter key, or a button to search and I cant figure out a way to only call the search method on enter when using OnChange(). <div class="form-group"> <TelerikTextBox Id="look-up-value" @bind-Value="LookUpValue" Class="form-control" OnChange="(async ()=> { await LookUpShipment(); })"></TelerikTextBox> </div> <TelerikButton Class="btn" Primary="true" OnClick="LookUpShipment">@TranslationService[Label.Search]</TelerikButton>

## Answer

**Svetoslav Dimitrov** answered on 25 May 2020

Hello Luke, To use such behavior, clicking Enter key or button, you can attach event handlers to capture the DOM events. There is an knowledge base article related to this (link: [https://docs.telerik.com/blazor-ui/knowledge-base/inputs-handle-keyboard-events](https://docs.telerik.com/blazor-ui/knowledge-base/inputs-handle-keyboard-events) ). By going this approach you would not need to use the OnChange event. Regards, Svetoslav Dimitrov
