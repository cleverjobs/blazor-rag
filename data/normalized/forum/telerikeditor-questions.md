# TelerikEditor questions

## Question

**Rob** asked on 10 Mar 2025

Is there a way to add a stylesheet to the prosemirror in the iframe? I want to add a plugin for a Placeholder eg: [https://gist.github.com/amk221/1f9657e92e003a3725aaa4cf86a07cc0](https://gist.github.com/amk221/1f9657e92e003a3725aaa4cf86a07cc0) Also: is there a way to let the user change the height of the TelerikEditor, just like with a text area (bottom right corner)?

## Answer

**Hristian Stefanov** answered on 11 Mar 2025

Hi Robert, Both of your questions are already covered by two existing feature requests: Add the ability to inject CSS files into the iframe Resizable Editor I've voted for both on your behalf and raised their priority. You can also subscribe to them to receive email updates on any progress. Regards, Hristian Stefanov

### Response

**Robert** answered on 11 Mar 2025

Tthx Hristian ! Another question: I try to insert a plugin but get the error: Microsoft.JSInterop.JSException: Failed to construct 'Plugin': Illegal constructor I guess it's because the Plugin type is not available in the Blazor component. Is there a way to solve this? <script suppress-error="BL9992"> window. pluginsProvider=( args )=> { const schema=args. getSchema (); const placeholder=( text )=> { const update=( view )=> { if (view. state. doc. textContent ) {
view. dom. removeAttribute ( 'data-placeholder' );
} else {
view. dom. setAttribute ( 'data-placeholder', text);
}
}; return new Plugin ({ view ( view ) { update (view); return { update };
}
});
}; return [...args. getPlugins (schema), placeholder ( 'Some text' )];
}
</script> <TelerikEditor Tools="@Tools" Plugins="pluginsProvider"> </TelerikEditor>

### Response

**Hristian Stefanov** commented on 12 Mar 2025

Hi Robert, The error " Failed to construct 'Plugin': Illegal constructor " is coming from how the Plugin is being instantiated. In ProseMirror, the Plugin class needs to be accessed through args.ProseMirror.Plugin, rather than calling new Plugin({...}) directly. For more details on how to insert a plugin, please have a look at the " Adding a Custom Plugin " article in our documentation. Kind Regards, Hristian

### Response

**Robert** commented on 13 Mar 2025

cool, thx totally missed that one!
