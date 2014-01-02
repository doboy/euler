// Generates the README.md file in the root directory from
// {language}/README.md files

class Problem(val number: Int) {
  var solutions : List[Solution] = List()

  def generate_html() : String = {
    var backgroundColor = "#FFF"
    var title = "Unsolved"
    if (solutions.length != 0) {
      backgroundColor = "#CEE7B6"
      val bestSolution = solutions.max
      val language = bestSolution.language
      val execution_time = bestSolution.execution_time
      title = s"Solve in $execution_time ms with $language"
    }

  s"""    <td style="width:20px;height:20px;vertical-align:middle;background-color:$backgroundColor;">
      <a style="text-decoration: none; color:#000" title="$title" href="http://projecteuler.net/problem=$number">
        <div style="font-size:70%;text-align:center;color:#000;cursor:pointer;">
          $number
        </div>
      </a>
    </td>"""
  }
}

class Solution(val language: String, val execution_time: Float) extends Ordered[Solution]{
  def compare(that: Solution) = {
    if (execution_time - that.execution_time <= 0) {
      -1
    } else {
      1
    }

  }
}

object generate_html {
  val questions = 400
  val questions_per_line = 20
  val problems = Range(0, questions + 1).map(new Problem(_))
  val readme_regexp = """problem (\d+): Solved in (\d+.\d+)ms""".r
  val friend_key = "67894488177272_b3f57d3674eea31e6069b8800b331508"

  def main(args: Array[String]) {
    for(language <- List("python", "haskell", "scala")) {
      val readme = scala.io.Source.fromFile(language + "/README.md").mkString
      for (solved <- readme_regexp findAllMatchIn readme) {
        val problem_number = solved.group(1).toInt
        if (problem_number < questions) {
        val execution_time = solved.group(2).toFloat
        val solution = new Solution(language, execution_time)
        problems(problem_number).solutions = solution :: problems(problem_number).solutions
        }
      }
    }

  println("""<!DOCTYPE html>
<html>
  <head>
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="chrome=1">
    <link href='https://fonts.googleapis.com/css?family=Chivo:900' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" type="text/css" href="stylesheets/stylesheet.css" media="screen" />
    <link rel="stylesheet" type="text/css" href="stylesheets/pygment_trac.css" media="screen" />
    <link rel="stylesheet" type="text/css" href="stylesheets/print.css" media="print" />
    <!--[if lt IE 9]>
    <script src="//html5shiv.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->
    <title>Euler by Doboy</title>
  </head>

  <body>
    <div id="container">
      <div class="inner">

        <header>
          <h1>Project Euler</h1>
          <h2>doboy's progress</h2>
        </header>

       <section id="downloads" class="clearfix">
          <a href="https://github.com/Doboy/euler" id="view-on-github" class="button"><span>View on GitHub</span></a>
        </section>

        <section id="main_content">
          <table border="1"><tbody>""")

    problems.drop(1).grouped(questions_per_line).foreach({
      chunk =>
         println("  <tr>")
         chunk.foreach({
           problem =>
             println(problem.generate_html)
         })
         println("  </tr>")
    })

    println("""</tbody></table>""")

    println("""<p>""")
    for(language <- List("python", "haskell", "scala")) {
      val problem_solved = problems.flatMap(_.solutions).filter(_.language == language).length
      println(s"<span><strong>$problem_solved</strong> problem solved in $language</span><br/>")
    }
    println("""</p>""")

    println("""<p>friend key: <code>67894488177272_b3f57d3674eea31e6069b8800b331508</code></p>
        </section>""")

    println("""</div>
    </div>
  </body>
</html>""")

  }
}

generate_html.main(Array())
