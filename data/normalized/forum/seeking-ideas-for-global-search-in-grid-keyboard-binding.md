# Seeking ideas for global search in grid keyboard binding

## Question

**Mar** asked on 02 Dec 2021

Hi I would like something similar to the search in bootstrap doc where you can type CTRL+/ to set focus in the search field. Are there any components/utils I can use in the Telerik Blazor lib? Found this jsakamoto/Toolbelt.Blazor.HotKeys: This is a class library that provides configuration-centric keyboard shortcuts for your Blazor WebAssembly (client-side) apps. (github.com)

### Response

**Martin Herløv** commented on 02 Dec 2021

I got the hotkeys working but I am having trouble setting focus on the GridSearchBox <GridSearchBox @Id="xxxxxxx" @ref="@GridSearchBoxElement" DebounceDelay="200" /> Have tried with @ref and Id. Id fails and the GridSearchBox don't have a focus property. The InputElement has a FocusAsync method await this.InputElement.FocusAsync(); Can I cast to InputElement

## Answer

**Svetoslav Dimitrov** answered on 07 Dec 2021

Hello Martin, I consider your request for a programmatic method to set the focus to the Grid search box as a very valid feature request. I have opened it on your behalf so that you are automatically subscribed to receive email notifications on status updates. I have, also, added your vote for it. In the meantime, you can use some JavaScript to focus on the search box. Regards, Svetoslav Dimitrov

### Response

**Martin Herløv** answered on 07 Dec 2021

Thanks looking forward to it (-: This is what I ended up with Some JS function focusElement ( selector ) { console.log( "focusElement: " + selector); let elem=document.querySelector(selector); if (elem && elem.focus) { setTimeout ( function ( ) {
elem.focus();
}, 30 );
}
} Then some C# using the Toolbelt.Blazor.HotKeys nuget package private void InitHotKeys ( ) {
HotKeysContext=HotKeys.CreateContext()
.Add(ModKeys.Ctrl, Keys.K, SetFocusInGridSearchField, "Set focus in grid search field" );
} private async Task SetFocusInGridSearchField ( ) { await JsRuntime.InvokeVoidAsync( "focusElement", GridSearchBoxPortfolioListGrid);
}

### Response

**Svetoslav Dimitrov** commented on 10 Dec 2021

Hello Martin, I am happy to see that you have managed to find a solution until we expose a programmatic method to focus on the search box!
