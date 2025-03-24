#!/usr/bin/env ruby

require 'yaml'
require 'fileutils'

def clean_front_matter(file_path)
  content = File.read(file_path)
  front_matter = content.match(/^---\n(.*?)\n---\n/m)
  
  if front_matter
    yaml = YAML.load(front_matter[1])
    
    # Clean categories and remove empty ones
    if yaml['categories']
      yaml['categories'] = yaml['categories']
        .reject { |cat| cat.to_s.include?('#Import') || cat.to_s.strip.empty? }
        .compact
    end
    
    # Clean tags and remove empty ones
    if yaml['tags']
      yaml['tags'] = yaml['tags']
        .reject { |tag| tag.to_s.include?('#Import') || tag.to_s.strip.empty? }
        .compact
    end
    
    # Remove empty arrays
    yaml.delete('categories') if yaml['categories']&.empty?
    yaml.delete('tags') if yaml['tags']&.empty?
    
    # Reconstruct the file content with proper YAML formatting
    new_front_matter = "---\n"
    yaml.each do |key, value|
      if value.is_a?(Array)
        new_front_matter += "#{key}:\n"
        value.each do |item|
          new_front_matter += "  - #{item}\n"
        end
      else
        new_front_matter += "#{key}: #{value}\n"
      end
    end
    new_front_matter += "---\n"
    
    new_content = content.sub(/^---\n.*?\n---\n/m, new_front_matter)
    File.write(file_path, new_content)
    puts "Fixed #{file_path}"
  end
end

# Process all markdown files in collections/_posts
Dir.glob('collections/_posts/*.markdown').each do |file|
  clean_front_matter(file)
end 