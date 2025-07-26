# Editor: del and ins html tag not valid

## Question

**Cla** asked on 13 Jan 2022

Hi, I would like to build a Telerik Editor which shows users the changes made in the editor. some of the HTML tag I think useful are:- "ins" and "del". However, when pasted my HTML, the "ins" tag seems to be automatically removed. Could you advise why and how i could resolve this issue? Code entered using "View HTML" button <del class='diffmod'> ended </del> <ins class='diffmod'> January </ins> HTML showing as below (January should be highlighted but its not) <p> <del> ended </del> January </p> Many thanks!

## Answer

**Svetoslav Dimitrov** answered on 17 Jan 2022

Hello Claris, The Editor provides a schema of supported tags, where you can see every supported tag, or add a new one. As part of your 2.29.0 version, we have distributed our source code. The schema.js file is located in the config folder of the editor. Depending on where you extracted the JavaScript portion of the code, the path would be: ....telerik-blazor/src/editor/config/schema.js The reason why the Editor does not currently support the <ins> tag as it is part of the Track Changes functionality that is not yet available. Regards, Svetoslav Dimitrov
