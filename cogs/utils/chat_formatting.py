def pagify(text, delims=["\n"], *, escape_mass_mentions=True, shorten_by=8, page_length=2000):
  in_text = text
  if escape_mass_mentions:
    num_mentions = text.count("@here") + text.count("@everyone")
    shorten_by += num_mentions
  page_length -= shorten_by
  while len(in_text) > page_length:
    closest_delim = max([in_text.rfind(d, 0, page_length) for d in delims])
    closest_delim = closest_delim if closest_delim != -1 else page_length
    if escape_mass_mentions:
      to_send = escape(in_text[:closest_delim], mass_mentions=True)
    else:
      to_send = in_text[:closest_delim]
    yield to_send
    in_text = in_text[closest_delim:]
  if escape_mass_mentions:
    yield escape(in_text, mass_mentions=True)
  else:
    yield in_text

def escape(text, *, mass_mentions=False, formatting=False):
  if mass_mentions:
    text = text.replace("@everyone", "@\u200beveryone")
    text = text.replace("@here", "@\u200bhere")
  if formatting:
    text = (
      text.replace("`", "\\`")
          .replace("*", "\\*")
          .replace("_", "\\_")
          .replace("~", "\\~")
    )
