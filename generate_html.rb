require 'erb'
require 'enumerator'

class Problem
  attr_accessor :solutions, :number

  def initialize(number)
    @number = number
    @solutions = []
  end

  def best_solution
    @solutions.max_by { |solution| solution.execution_time }
  end

  def solved?
    @solutions.length != 0
  end
end

class Solution
  attr_accessor :execution_time, :language

  def initialize(language, execution_time)
    @language = language
    @execution_time = execution_time
  end
end

class IndexHtml
  def initialize(problems, template, filename)
    @problems = problems
    @template = template
    @filename = filename
    @problem_chunks = @problems.each_slice(20).map
    @solutions_pre_language  = @problems.map {
      |problem| problem.solutions
    }.flatten.group_by {
      |solution| solution.language
    }.sort_by {
      |language, solutions| solutions.length
    }

  end

  def render
    ERB.new(@template).result(binding)
  end

  def save
     File.open(@filename, "w+") do |f|
      f.write(render)
    end
  end
end

def main
  problems = 1.upto(300).map { |number| Problem.new(number) }
  readme_regexp = /problem (\d+): Solved in (\d+.\d+)s/

  ["python", "haskell", "scala", "ruby"].each do |language|
    contents = File.read("#{language}/README.md")
    contents.scan(readme_regexp).each do |match|
      number = match[0].to_i
      execution_time = match[1].to_f
      solution = Solution.new(language, execution_time)
      problems[number - 1].solutions << solution
    end
  end

  template = File.read("index.html.erb")
  IndexHtml.new(problems, template, "index.html").save
end

main
