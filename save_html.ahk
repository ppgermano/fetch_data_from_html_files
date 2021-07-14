#Persistent
return

OnClipboardChange:
ToolTip Clipboard data type: %A_EventInfo%
Fileappend,%clipboard%,C:\Users\User\Your\Path\Here\src\html_data`\%A_Now%`.html
/*Send !{Tab}*/
ToolTip  ; Turn off the tip.
return
