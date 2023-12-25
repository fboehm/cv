function Header(elem)
  if elem.level == 2 then
    -- Print the level 2 heading text
    print("Heading Text:", elem.content)

    -- Check if elem.classes exists
    if elem.classes then
      -- Iterate over the elements in elem.classes and print each one
      for _, class in ipairs(elem.classes) do
        print("Class:", class)
      end
    else
      print("No classes found.")
    end
  end
  return elem
end
