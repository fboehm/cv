-- colorize_and_format_headings.lua

function Header(elem)
    local style = ""
    
    -- Check if the header has a "blue" class
    if elem.classes:includes('blue') then
        style = style .. "color: blue;"
    end

    -- Check if the header has a "large" class
    if elem.classes:includes('large') then
        style = style .. "font-size: 1.5em;"
    end

    -- Check if the header has a "smallcaps" class
    if elem.classes:includes('smallcaps') then
        style = style .. "font-variant: small-caps;"
    end

    -- Apply the combined style to the header
    if style ~= "" then
        elem.attributes = { style = style }
    end
    return elem
end
