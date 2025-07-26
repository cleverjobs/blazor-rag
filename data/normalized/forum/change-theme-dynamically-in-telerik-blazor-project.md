# Change theme dynamically in telerik blazor project

## Question

**Mil** asked on 20 Aug 2022

Hello, I referred the following link - [https://docs.telerik.com/blazor-ui/knowledge-base/change-theme-runtime](https://docs.telerik.com/blazor-ui/knowledge-base/change-theme-runtime) Attaching the project where in I have tried to implement the code but its not working. Trying to resolve since last 3 to 4 days but unable to get solution. Can someone put me in correct direction. Thanks & regards, Milinnd

### Response

**Robert C** commented on 20 Aug 2022

I am doing the same and it definitely works. Double check your code, especially the JS. Put breakpoints to make sure its being hit. See if theres any browser console errors.

### Response

**Milind** commented on 22 Aug 2022

Hello Robert, Thanks for clue. I had missed the "id" tag for link statement. Now its working. One quick question - When I used to have theme manager on web form, changing the theme used to affect the entire page, including background color. Where as here it only affects the controls on the page, it doesn't change the page background color. It remains white only. e.g. if I select "Dark" theme it do not change the page background to black. Is it the same way working at your end ? If not, can your suggest to get it working? Thanks & regards, Milind

### Response

**Robert C** commented on 22 Aug 2022

Most likely you have some custom css rules that override the background to make it white. Check Dev Tools to see where the background is coming from.

### Response

**Milind** commented on 23 Aug 2022

Hello Robert, Thanks for input, but could not find any thing specific related to background colour. Thanks & regards, Milind
