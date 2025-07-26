# After Render error variable is null

## Question

**Vis** asked on 21 Dec 2021

Hi, After submiting the form, On error handling in Catch, the execption is assign to variable error After render the vairable error is null Could please help how to assign execption value to variable error after render Please see below code. @{ string error { get; set; } protected override void OnInitialized ( ) { try {}
finaly{}
} async protected override Task OnAfterRenderAsync ( bool firstRender ) { var relativeUri=navigationManager.Uri; var uri=navigationManager.ToAbsoluteUri(relativeUri); if (firstRender){} if (QueryHelpers.ParseQuery(uri.Query).TryGetValue( "isSessionTimeout", out var tempTimeout))
{
notification?.ShowError(error); //error="Session timed out"; showToast=true;
}
} async Task OnSubmit ( ) { try {

}

catch(exception ex){
error=ex.ToString();
}

}
}

### Response

**Vishnu** commented on 23 Dec 2021

Hi Team, Please guide on above issue. Thanks

### Response

**Vishnu** commented on 04 Jan 2022

Hi, Could you please update on the same Thanks, Vishnu Vardhanan
