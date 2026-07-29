from schemas.optimized_resume import OptimizedResume



def write_markdown(
    resume: OptimizedResume,
    output_path: str
):

    content = []


    # 基本信息

    content.append(
        f"# {resume.name}"
    )


    # 技能

    content.append(
        "\n## Skills\n"
    )


    for skill in resume.skills:

        content.append(
            f"- {skill}"
        )


    # 教育

    content.append(
        "\n## Education\n"
    )


    for edu in resume.education:

        content.append(
            f"- {edu}"
        )


    # 经历

    content.append(
        "\n## Experience\n"
    )


    for exp in resume.experiences:

        content.append(
            f"- {exp}"
        )


    # 项目

    content.append(
        "\n## Projects\n"
    )


    for project in resume.projects:

        content.append(
            f"- {project}"
        )


    # 修改说明

    content.append(
        "\n## Modification Notes\n"
    )


    for note in resume.modification_notes:

        content.append(
            f"- {note}"
        )


    markdown = "\n".join(content)


    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(markdown)


    return output_path