# data in textarea control in browser html.

## Question

**Law** asked on 17 Aug 2021

HTML for textarea does not contain the data bound to it-- how is this being displayed in the browser and is there any way to see the contents of the textarea via the html? When i inspect the html for a text area it doesn't contain the actual data-- it contains a data id reference (I'm assuming this). I am trying to "export" an html page using JavaScript code like this: document.getElementsByClassName('targetForExport')[0].outerHTML I have also used innerHTML and it doesn't matter. BUT there is no data in the textareas and the datepickers. Ultimately i'm trying to export a page (set of html elements really) to a PDF format. The only real catch i'm running into is the data simply isn't there. Thanks.

## Answer

**Matthias** answered on 17 Aug 2021

Hi Lawrence, As far as I understand the question, the data is displayed, but you only find the reference. I assume that it is a Blazor server application. It communicates via SignalR. You can find more about it here: Hosting models However, I'm not sure I understood you correctly best regards Matthias

### Response

**Lawrence** commented on 17 Aug 2021

Thank you Matthias. My sentence is a bit incomplete above. What i'm saying is the html doesn't contain the data-- for instance a textarea tag would normally contain the data between the opening and closing tags but what i'm finding is the html tags are empty but that there is a data-id reference. In reading the article you linked to it seems to suggest that the static html is replaced with "interactive elements" that i can only assume contain the data and probably enough code to allow for binding and other things for which the framework is responsible. Having said that it sounds like there is no reasonable way to get the html content for a blazor html tag in at least some circumstances and i'll have to generate the form from my own mechanism. I'm assuming that Telerik doesn't have a way to "export" a "telerikwindow" to PDF at this point. Any suggestions for trying to export an html form to PDF or some other format? Thanks.

### Response

**Matthias** commented on 17 Aug 2021

I use the following library for these purposes HTML2Canvas I'm away now for the next few days, but can send you an example next week of how to use the library with Blazor

### Response

**Lawrence** commented on 17 Aug 2021

Thank you-- but would this work for a blazor server app? Have a nice time off Matthias! LT

### Response

**Matthias** commented on 17 Aug 2021

Yes, I use it as well. But it is quite possible that there is a simpler solution. For example, you can also use Telerik Document Processing Libraries. Depending on what you need, one or the other makes more sense. If it should be only a screenshot, then HTML2Canvas is the fast way

### Response

**Lawrence** commented on 23 Aug 2021

Hello Matthias, Can you send me or point me to a working example? I spent some time and really couldn't find one for blazor. I don't like the idea of using javascript directly actually. Thanks! Lawrence

### Response

**Lawrence** commented on 25 Aug 2021

Hello again Matthias, Are you back from your time off yet? I was hoping you had a working version of the html2canvas in c#/blazor. I can probably do a javascript version but would rather use c# if at all possible and especially if there is a way to use c#. Thanks.

### Response

**Matthias** answered on 26 Aug 2021

Hi Lawrence, I am still on vacation, but have some time to send you a possible solution. I thought that you have already found a way. First install html2canvas. Then create another JavaScript file or insert the code in a suitable place (for example :_Host.cshtml or index.html). Here is the code: Javascript: function downloadScreenShot ( filename,selector ) {
html2canvas( document.querySelector(selector)).then( canvas=> {
saveAs(canvas.toDataURL(), filename + '.png' )
});
} function saveAs ( uri, filename ) { var element=document.createElement( 'a' ); if ( typeof element.download==='string' ) {
element.href=uri;
element.download=filename; document.body.appendChild(element);
element.click(); document.body.removeChild(element);
} else { window.open(uri);
}
} razor (example) <div id="myDiv"> <TelerikGrid Data="@Customers" Height="100%" Pageable="true" PageSize="15" Resizable="true" Sortable="true" Navigable="true" ScrollMode="GridScrollMode.Scrollable" ShowColumnMenu="true"> <GridColumns> <GridColumn Field="@(nameof(customer.CustName))" Visible="false" /> <GridColumn Field="@(nameof(customer.CustCity))" Width="80px" Visible="false" /> <GridColumn Field="@(nameof(customer.CustPhone))" /> </GridColumns> </TelerikGrid> </div> code private async Task downloadScreenShot ( ) { await js.InvokeVoidAsync( "downloadScreenShot", "screenshot", "#myDiv" );
} I hope that I could help you a little bit with this. In principle, a stream can also be returned. However, in my experience, at least with Blazor Server, this is a time problem.

### Response

**Matthias** commented on 26 Aug 2021

by the way, you can of course also use "async void" here

### Response

**Matthias** commented on 26 Aug 2021

I forgot an example :)

### Response

**Lawrence** commented on 26 Aug 2021

Hello Matthias, Thank you very much and sorry to bother you on your vacation--- i thought you were back and would be back by now. Previously i had rejected using javascript and was hoping to use the wisej objects in c# directly but was not able to get that to work. I assumed the javascript would work and was able previously to get the html via that method. I guess i'll just have to stick with the javascript method and leave it at that. I was wondering about how canvas2html doesn't seem to be able to deal with wrapped content correctly. For instance i have a textarea (telerik of course!) and it properly wraps text as it should but for some reason html2canvas doesn't see that the text has been wrapped and just cuts it off (funny in a way). Was just wondering if you have seen this and have a solution. Thanks again....

### Response

**Lawrence** commented on 26 Aug 2021

Matthias, I decided to set the autosize="true" for the textareas and that will work for me. Thank you so much for your help and hope your vacation is wonderful!
