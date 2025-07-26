# wrap carousel buttons

## Question

**EdEd** asked on 27 Feb 2023

Is there a way to do this? Right now, if you have too many, they just run off the screen. Thanks... Ed

## Answer

**Nadezhda Tacheva** answered on 02 Mar 2023

Hi Ed, You can wrap the page buttons with some custom CSS targeting the "k-scrollview-nav" element. Here is an example configuration: [https://blazorrepl.telerik.com/mnEnkcFl074Lf7ec57.](https://blazorrepl.telerik.com/mnEnkcFl074Lf7ec57.) You may alter the styles as needed to achieve the desired result depending on the scenario and image count. As a side note, the pager should generally be scrollable. Thus, when the user selects the last visible page, the pager will scroll to show the remaining page buttons. See the example in the jQuery version of the component: [https://demos.telerik.com/kendo-ui/scrollview/api.](https://demos.telerik.com/kendo-ui/scrollview/api.) This functionality is missing in the UI for Blazor Carousel, so I opened a bug report on your behalf: [https://feedback.telerik.com/blazor/1599734-carousel-with-multiple-pages-does-not-show-all-page-buttons](https://feedback.telerik.com/blazor/1599734-carousel-with-multiple-pages-does-not-show-all-page-buttons) I also added your vote to bump its popularity as we prioritize the fixes based on the demand along with their severity. As a creator, you are automatically subscribed to get status updates. I also rewarded your account with some Telerik points as a small token of appreciation for pointing our attention to this behavior. Last but not least, I'd like to ask you for some feedback for the Carousel pager in this scenario. When the Carousel has a lot of pages (e.g. 50) would you consider the current paging option as useful or you'd prefer another alternative? For example, display the page number as a part of a total - page 1 of 50. Or you'd even prefer an option for customizing the pager and specify your desired UI? Please feel free to share any thoughts you may have on the matter. Regards, Nadezhda Tacheva Progress Telerik
