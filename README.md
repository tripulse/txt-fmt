## TXT1: Ain't an text-encoding format.

TXT1 is container to contain text with several encodings (i.e UTF8, UTF16). It's metadata based container. Currently, it supports 9 types of encodings.
Including 7 variants of Unicode.

#### Encodings it supports:
- ASCII
- CP037
- UTF-8
- UTF-16
- UTF-32
- UTF-16-LE
- UTF-16-BE
- UTF-32-LE
- UTF-32-BE

> `LE` means **little-endian**; `BE` means **big-endian**.

---

#### Why use it?
Suppose that, you've encoded a string (`சியர்ஸ் வரவேற்பு`) in UTF-16 and you wrote it in a FILE.
In that file there's no metadata of the encoding of string. Another text editor (i.e kate) opens it in UTF-8.

It would be just a gibberish (`��������� `) in that text-editor.
To avoid this We've designed this container to contain metadata to parse and the text with it.

---

#### Licensing
MIT License.
