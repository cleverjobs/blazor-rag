# Open PdfViewer with highlighted text

## Question

**eli** asked on 15 Sep 2022

In the new PdfViewer, is there a feature to have a document opened with some text highlighted?

### Response

**eliyahu** commented on 19 Sep 2022

Looking more into the PdfViewer, I realized that there is no programmatic control whatsoever over the viewed content. No way to highlight text from the code, everything is interactive. Telerik, is that correct?

### Response

**Hristian Stefanov** commented on 20 Sep 2022

Hi Eliyahu, Indeed, it sounds interesting to have an option to highlight text in the PdfViewer. I will, for sure, share the idea about a built-in feature in the component that will allow you to more easily achieve the desired result with our development team. If, as a result of the discussion, the feature turns out very well/feasible for the PdfViewer, I will open a public item on our Public Feedback Portal. At this stage, the possible approach to highlight text on file open is to use a Javascript function on the desired text by targetting the correct HTML element in the OnAfterRender event handler and applying yellow background. I will get back to you here with the results of our discussion very soon (by the end of the week at the latest). In the meantime, if further questions or suggestions appear, please let me know. Kind Regards, Hristian

### Response

**eliyahu** commented on 20 Sep 2022

Thanks, Hristian, sounds good. One problem with the Javascript/HTML approach is that the PdvViewer DOM may change with new releases and the Javascript may become broken.

### Response

**Stamo Gochev** commented on 23 Sep 2022

Hi Eliyahu, Can you provide more details on why you need this functionality - what is the exact scenario that you want to cover? In the general case, selection over a standalone text, input text, etc. is mainly done through an interaction (the end user selecting the text). If you want a certain text to be selected, then using browser APIs for selection is the way to go (similar to selecting any text on a page). On the other hand, if you are just interested in highlighting a certain part of the text, then another approach is to edit your PDF document beforehand using the appropriate software (e.g. add a background color to a certain section), which will result in highlighting it. Note that this type of highlight will be permanent though, so the approach with JS might be more applicable in your case (and yes, it is expected for you to keep track of changes to the DOM and reapplying the highlight).

### Response

**eliyahu** commented on 23 Sep 2022

Ok, the use case is simple. In our application, we provide searching across large number of documents. The user gets search results as a list of documents and opens one of them. At this point, we want to open the document with the text used in the search highlighted. Your second approach won't work for use. Using browsing API will work, but the concern is about changes in DOM on Telerik end.

### Response

**Stamo Gochev** commented on 26 Sep 2022

Hi Eliyahu, As far as I understand the explanation, what I can currently suggest is using the browser selection APIs and manually keeping track of what to select and when - similar to what should be done if you want to select certain parts of any HTML page. Another approach that might be easier for you to implement is to open the search panel and manually type the contents of the search term, e.g.: // click the search button in the toolbar var searchButton=document.querySelector( ".k-i-search" );
searchButton.click(); setTimeout ( function ( ) { // find the search input var searchInput=document.querySelector( ".k-search-panel input" );

searchInput.focus(); // set the search value searchInput.value="some value"; // trigger the "change" event to display the found text searchInput.dispatchEvent( new Event( 'change' ));
}, 1000 ); This will display the search results as if the user has searched for them beforehand and show the built-in highlighting of the text.
