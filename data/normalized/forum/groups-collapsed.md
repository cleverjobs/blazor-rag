# Groups collapsed

## Question

**Ric** asked on 23 Oct 2019

I am pretty sure i can just write a JavaScript function to go back and find/collapse all the groups in the grid but is there a grid setting where I can just collapse them by default?

## Answer

**Marin Bratanov** answered on 24 Oct 2019

Hello Rick, At the moment programmatic control over grouping is not implemented yet, you can track it here (I added your Vote and feedback): [https://feedback.telerik.com/blazor/1432800-set-grouping-from-code.](https://feedback.telerik.com/blazor/1432800-set-grouping-from-code.) Regards, Marin Bratanov

### Response

**Rick** answered on 24 Oct 2019

Is there a way that I can assign the id to the grid so that I can assign an id to the grid so that I can possibly manipulate it using jQuery?

### Response

**Marin Bratanov** answered on 24 Oct 2019

Hello Rick, It is not possible, at least at the moment. Manipulating components with JS is not the Blazor way and if you want to do that, I suggest you wrap the grid in an element you can uniquely identify and traverse the DOM through that instead. Or, just use the .k-grid class the grid wrapping element has (you could add a custom Class too). Regards, Marin Bratanov

### Response

**Rick** answered on 24 Oct 2019

I was going to port a mvc app I have to blazor but maybe I will just wait until you have the group manipulations in. I need it to do like attached.

### Response

**Marin Bratanov** answered on 24 Oct 2019

Hello Rick, Right now, the Blazor grid does not offer this much API and flexibility, it's still under a year old and has some catching up to do. Regards, Marin Bratanov
