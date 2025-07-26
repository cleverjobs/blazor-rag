# Centre "Loading" animation in visible part of browser window

## Question

**PHPH** asked on 14 Mar 2021

Trying the LoaderContainer component, and it's really great. I have quite a tall Grid component, and when triggering a long action from the top or bottom rows of the grid, the spinner animation and "Loading" text is not visible unless you scoll to the vertical centre of the grid where it's actually being rendered. The dark overlay does show and that's probably enough to indicate something's happening on the back end, but is there an easy way to make this animation show in the centre of the visible part of the browser window? Thanks, Peter

## Answer

**Lachezar Georgiev** answered on 17 Mar 2021

Hello Peter, To achieve that effect, you could use custom CSS to style the loader panel - the white rectangle that wraps the loader indicator. I've attached a sample project that will allow you to do just that. The project includes two pages: Index - This page uses the grid's built-in loader container. ExternalLoader - This page uses an explicitly defined loader container in its razor file. Aside from that, the only real difference in the CSS is the selectors of the loader panel. You will find them in the code. Note that the sample project is built on top of the project mentioned in the Block all content article from the docs. Here is the link to project repo. Regards, Lachezar Georgiev Progress Telerik
