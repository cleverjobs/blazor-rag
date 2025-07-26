# Readyonly Stepper

## Question

**Eri** asked on 03 Aug 2022

Is there a way to use the stepper in a view only mode? I am using it to show the current status in a larger process, so the user shouldn't be able to click to change the value. Thanks in advance

## Answer

**Dimo** answered on 05 Aug 2022

Eric, yes, use one-way binding for the Value and a ValueChanged handler, which does not update it, as it normally should. Stepper Step Index: <TelerikNumericTextBox Min="0" Max="6" @bind-Value="@CurrentStep" Width="100px" /> <div class="no-focus"> <TelerikStepper Value="@CurrentStep" ValueChanged="@ValueChangeHandler"> <StepperSteps> <StepperStep Text="1" Label="Step 1"> </StepperStep> <StepperStep Text="2" Label="Step 2"> </StepperStep> <StepperStep Text="3" Label="Step 3"> </StepperStep> <StepperStep Text="4" Label="Step 4"> </StepperStep> <StepperStep Text="5" Label="Step 5"> </StepperStep> <StepperStep Text="6" Label="Step 6"> </StepperStep> <StepperStep Text="7" Label="Step 7"> </StepperStep> </StepperSteps> </TelerikStepper> </div> <style> /* optional - prevent focus on click */.no-focus { pointer-events: none;
} </style> @code {
int CurrentStep { get; set; } public void ValueChangeHandler ( int newStep ) {

}
} Regards, Dimo
