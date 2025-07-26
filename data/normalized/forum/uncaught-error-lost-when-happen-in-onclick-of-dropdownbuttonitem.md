# Uncaught error lost when happen in OnClick of DropDownButtonItem

## Question

**Dav** asked on 16 Jul 2024

Hello, I'm having an hard time to understand why my error arent showing in my blazor app when they happen inside the OnClick event of an DropDownButtonItem. I've joined some code to reproduce the problem. When you click on "twitter" inside the Share DropDownButton, you should be able to see the "System.Exception" in the console log of the browser (f12) but nothing happen. I can clearly see the "1" from the Console.WriteLine right before it but not the exception. In my program, I was expecting to see our custom error handling to catch that error and show an error message to the client, but instead, nothing happen since we dont know the code failed, nor do we receive any answer Thank you <div class="demo-section auto">
<TelerikDropDownButton Icon="@SvgIcon.Share">
<DropDownButtonContent>Share</DropDownButtonContent>

<DropDownButtonItems>
<DropDownButtonItem Icon="@SvgIcon.Twitter" OnClick="@(()=>OnItemClick(" Twitter "))">Twitter</DropDownButtonItem>
</DropDownButtonItems>

</TelerikDropDownButton>
</div>

@code { private void OnItemClick ( string item ) {
Console.WriteLine( 1 ); throw new System.Exception();
Console.WriteLine( 2 );
}
}

## Answer

**Nadezhda Tacheva** answered on 18 Jul 2024

Hi David, I suspect that you are hitting this bug: Exception thrown in the OnClick event of the Menu is not caught by ErrorBoundary. The item is initially opened for the Menu but also targets other similar components including popups such as the DropDownButton or the SplitButton where exceptions thrown in the OnClick event of the children in the popup are not caught by the ErrorBoundary. You may vote for the item and follow it to keep track of its progress. Currently, the only alternative that I can suggest is to handle the DropDownButtonItem click with the conventional try-catch block. I apologize for the inconvenience this bug may be causing on your side. Regards, Nadezhda Tacheva
