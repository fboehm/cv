function format_author_name(citation)
  if citation.author and #citation.author > 0 then
    for i, author in ipairs(citation.author) do
      if author.family and (author.family == "Boehm") then
        local formatted_name = pandoc.Strong(pandoc.Person(author.given, author.family))
        citation.author[i] = formatted_name
      end
    end
  end

  return citation
end

function Citation(c)
  return format_author_name(c)
end
