# Wizard Stepper - how to cusomize starting step of wizard.

## Question

**Bee** asked on 29 Apr 2022

Hello, I would like to programmatically change what is going to be the first step of the wizard. For example, on my page I have 2 buttons, if the user clicks the first button, then the wizard should open at step 1, and if the user clicks the second button then the wizard should skip step 1, and directly open at step 2. Is there a way to set the starting step of the wizard conditionally. Like an active index/step to know which step the wizard is at or a property like startindex to indicate the starting step of the wizard. Your help is really appreciated Beena.

## Answer

**Svetoslav Dimitrov** answered on 04 May 2022

Hello Beena, You can preset the Value parameter of the Wizard so it starts from a step different than the first one. From this REPL link, you can see a Proof of Concept and you can extend this example for your actual application. Regards, Svetoslav Dimitrov Progress Telerik
