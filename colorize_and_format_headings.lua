-- colorize_and_format_headings.lua

function Header(elem)
    print("elem.level: " .. elem.level)
    print("elem.classes: " .. tostring(elem.classes))
    print("elem.content: " .. tostring(elem.content))
    if elem.level == 2 then
        -- Check if the header has a "blue" class
        if elem.classes:includes('blue') then
            table.insert(elem.content, 1, pandoc.RawInline('latex', '\\textcolor{blue}{'))
            table.insert(elem.content, pandoc.RawInline('latex', '}'))
        end
        if elem.classes:includes('smallcaps') then
            table.insert(elem.content, 1, pandoc.RawInline('latex', '\\textsc{'))
            table.insert(elem.content, pandoc.RawInline('latex', '}'))
        end
        if elem.classes:includes('large') then
            table.insert(elem.content, 1, pandoc.RawInline('latex', '\\large{'))
            table.insert(elem.content, pandoc.RawInline('latex', '}'))
        end


    end
    return elem
end
