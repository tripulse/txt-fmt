## TXT1: Ain't an text-encoding format.

TXT1 is container to contain text with several encodings (i.e UTF8, UTF16). It's metadata based container. Currently, it supports 9 types of encodings.
Including 7 variants of Unicode.

#### Encodings it supports:
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


## ARCHIVED
The reason for archival is because I recently learned about *UTF-8* which resolves all of these problems by technique called **continiuation bytes**, this method is super effective and takes lesser space (i.e 24-bits = 3bytes). Decoders are able to interpret this. What I was talking about as *UTF-8* is actually *Windows-1252* encoding.

From this short description I gave you, you may understand why this library is bullshit and doesn't make any sense at all (nowadays). The entire idea I had in my mind was entirely baseless.
