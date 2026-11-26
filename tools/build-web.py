import sys
src=open(sys.argv[1],encoding='utf-8').read()
i=src.index('<style>'); j=src.index('</style>')+len('</style>')
head=src[:i].replace('<meta name="claude:viewport-fit-sides" content="cover">\n','')
style=src[i:j]; body=src[j:]
reps=[
 ("$('#ai-label').textContent = on ? 'AI coach live (Claude)' : 'Offline mode · rule-based coach';",
  "$('#ai-label').textContent = on ? 'AI coach live (Claude)' : (window.claude ? 'Offline mode · rule-based coach' : 'Web demo · rule-based coach');"),
 ('<a class="brand" href="#" data-act="home">', '<a class="brand" href="https://feedback-paths.vercel.app" title="Feedback Paths project page">'),
]
for a,b in reps:
    assert body.count(a)==1, a[:50]; body=body.replace(a,b)
reset="<style>\nhtml{color-scheme:light}\n:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}\nbody{margin:0;font-size:14px;font-family:system-ui,-apple-system,sans-serif}\nimg{max-width:100%}\n[hidden]{display:none!important}\n</style>\n"
out=('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
 '<meta name="description" content="Feedback Paths Studio: English learners discuss peer and AI feedback on their writing, with adaptive scaffolding, revision analysis and a teacher dashboard.">\n'
 + reset + head + style + '\n</head>\n<body>\n' + body.strip() + '\n</body>\n</html>\n')
open(sys.argv[2],'w',encoding='utf-8').write(out)
