# Trying to use TelerikEditor OnChange="@SomeMethod"

## Question

**Rol** asked on 21 Sep 2021

No matter what method signature I come up with, I always get a compile error like [CS1503] Argument 3: cannot convert from 'method group' to 'bool' I tried void SomeMethod(), void SomeMethod(object _), Task SomeMethod(), Task SomeMethod(object _), async Task ... I also tried <TelerikEditor OnChange="@(_=> SomeMethod())"> and variations thereof. Trying to use <TelerikEditor T="string"> does not work either. Any idea what I should be doing?

## Answer

**Nadezhda Tacheva** answered on 23 Sep 2021

Hello Roland, The reason behind this is that the Editor does not expose OnChange event - you can check the available events in the article that Nikolas linked - Editor Events. While the OnChange event is not something that the Editor supports (in Blazor and in other suites), exposing an OnBlur event seems like a valid enhancement. Therefore, I opened a feature request on your behalf in our public

### Response

**Roland** commented on 24 Sep 2021

> The reason behind this is that the Editor does not expose OnChange event Rider intellisense suggests OnChange and OnBlur because the base class TelerikInputBase supports it. I did not verify it in the API reference.> you want to convert the HTML to RTF on explicit demand Yes, but in code, not by a user, so no buttons needed, just an event (handler) I'll just wait for the OnBlur implementation. I have my own <HtmlEditor> wrapper, and that one exposes the sanitized content, so whenever I want I can have the latest content without an explicit Save or Blur event. Good enough.

### Response

**Nadezhda Tacheva** commented on 27 Sep 2021

Hi Roland, I am glad to find out this will suffice for your use case. Please let us know if you run across any other concerns, so we can step in and assist.

### Response

**Nikolas** answered on 21 Sep 2021

Hello Roland, Did you try with ValueChanged? <TelerikEditor ValueChanged="ValueChangedHandler"> </TelerikEditor> @code { void ValueChangedHandler ( string value ) {

Console.WriteLine( "ValueChanged fired" );
}
} Docs: [https://docs.telerik.com/blazor-ui/components/editor/events](https://docs.telerik.com/blazor-ui/components/editor/events) Regards, Nikolas

### Response

**Roland** answered on 21 Sep 2021

That event fires with every keypress and I need to convert the HTML to RTF. I only want to do that on explicit demand, or occasionally on events like OnChange and OnBlur.
