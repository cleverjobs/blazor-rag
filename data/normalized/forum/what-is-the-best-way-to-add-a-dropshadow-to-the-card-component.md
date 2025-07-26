# What is the best way to add a dropshadow to the Card component?

## Question

**Dav** asked on 04 Apr 2022

Something like this. Is it simply to wrap the card in a <div> and use css?

## Answer

**Dimo** answered on 07 Apr 2022

Hi David, The "best" way to add Card shadows can depend on your goals and preferences: If you want to style all Cards, then use the "native" Card CSS class. The CSS rule placement will determine if you target all Cards on the page or in the app. .k-card { box-shadow: 10px 10px 10px red;
} If you want to target specific Cards, then use a custom CSS class for these Card instances. Using container <div>s will produce the same result, but is probably not necessary. <TelerikCard Class="foo" /> <style>.foo { box-shadow: 10px 10px 10px red;
} </style> I recommend these documentation articles: How to use CSS Isolation with Telerik Blazor components How to use custom CSS with Telerik Blazor components Regards, Dimo Progress Telerik
