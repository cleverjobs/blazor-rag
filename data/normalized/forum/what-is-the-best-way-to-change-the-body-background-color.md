# What is the best way to change the body background color?

## Question

**Dav** asked on 13 Apr 2022

I would like to change the background color of my web app from white to a light blue (#f4f7fc). I created a theme awhile back and still have the json file. So I uploaded that to the theme tool and changed the background and downloaded the new theme. I replaced the theme .css file in my application but there was no change. I can see the new color under the .k-body and a few other classes. But in the developer tools it seems that the background color on the <body> element is set to var(--bs-body-bg). Is this a Bootstrap variable? How can I override this?

## Answer

**Hristian Stefanov** answered on 18 Apr 2022

Hi David, It looks like the --bs-body-bg bootstrap class overrides the body color you've set. I see two possibilities here: Make the body color style!important to prevent the override from the bootstrap class. For example: .k-body { color: #424242; background-color: #f4f7fc!important;
} Inspect the elements (using browser DevTools ) and edit directly the current variable that takes care of the background color. Additionally, check out this article for more helpful information on such scenarios with bootstrap - Customize theme. I hope the above helps. I would be glad to keep me updated on the situation. Thank you. Regards, Hristian Stefanov
