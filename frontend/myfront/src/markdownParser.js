
//no idea on how this works but just copy it from chatgpt
import 'highlight.js/styles/github-dark.css';
import MarkdownIt from 'markdown-it';
import hljs from 'highlight.js';
import emoji from 'markdown-it-emoji';
import sub from 'markdown-it-sub';
import abbr from 'markdown-it-abbr';
import anchor from 'markdown-it-anchor';
import footnote from 'markdown-it-footnote';
import ins from 'markdown-it-ins';
import deflist from 'markdown-it-deflist';

const md = new MarkdownIt({
    html: true,
    breaks: true,
    linkify: true,
    highlight: function (str, lang) {
        if (lang && hljs.getLanguage(lang)) {
            try {
                return '<pre class="hljs"><code>' +
                    hljs.highlight(str, { language: lang, ignoreIllegals: true }).value +
                    '</code></pre>';
            } catch (error) {
                console.error(error);
            }
        }

        return '<pre class="hljs"><code>' + md.utils.escapeHtml(str) + '</code></pre>';
    }
}).use(emoji).use(sub).use(abbr).use(anchor).use(footnote).use(ins).use(deflist);

export default md;